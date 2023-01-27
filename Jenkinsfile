/*
File: Jenkinsfile
Author: Dalwar Hossain (dalwar23@pm.me)
Copyright: Dalwar Hossain
*/

pipeline {
    agent any
    environment {
        PYTHON_INTERPRETER = "python3.8"
        REPOSITORY_NAME = sh (script: 'echo $(echo `git config --get remote.origin.url` | rev | cut -d "/" -f 1 | cut -d "." -f 2 | rev)', returnStdout: true).trim()
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '1'))
    }
    stages {
        stage ('Sanity Check') {
            parallel {
                stage ('Check Python3') {
                    steps {
                        sh "${PYTHON_INTERPRETER} --version"
                    }
                }
                stage ('Python3 virtualenv') {
                    steps {
                        sh 'virtualenv --version'
                    }
                }
                stage ('Check Setup') {
                    steps {
                        sh 'test -f setup.py'
                        sh 'echo \$?'
                    }
                }
            }
        }
        stage ('Initialize') {
            steps {
                sh "virtualenv --always-copy -p ${PYTHON_INTERPRETER} venv"
                sh '''
                source venv/bin/activate
                pip install --upgrade pip setuptools wheel
                pip --version
                pip list
                '''
            }
        }
        stage ('Pre-Build') {
            parallel {
                stage ('Dev Dependencies') {
                    when {
                        expression {
                            fileExists('requirements_dev.txt')
                        }
                    }
                    steps {
                        sh '''
                        source venv/bin/activate
                        pip install -r requirements_dev.txt
                        deactivate
                        '''
                    }
                }
                stage ('Pkg Dependencies') {
                    when {
                        expression {
                            fileExists('requirements.txt')
                        }
                    }
                    steps {
                        sh '''
                        source venv/bin/activate
                        pip install -r requirements.txt
                        deactivate
                        '''
                    }
                }
            }
        }
        stage ('Build') {
            parallel {
                stage ('Build Source') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python setup.py build
                        deactivate
                        '''
                    }
                }
                stage ('Build HTML') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        cd docs/
                        make clean html
                        deactivate
                        '''
                    }
                }
                /*stage ('Build PDF') {
                     steps {
                        sh '''
                        source venv/bin/activate
                        cd docs/
                        make latexpdf LATEXMKOPTS="-silent -f -no-shell-escape"
                        deactivate
                        '''
                    }
                }*/
            }
        }
        stage ("Run Tests"){
            steps {
                sh '''
                source venv/bin/activate
                if [[ -d "${WORKSPACE}/build/" ]]; then
                    py.test --junitxml build/labelx_test_results.xml
                fi
                deactivate
                '''
            }
        }
        stage ('Package') {
            parallel {
                stage ('Source') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python setup.py egg_info --tag-build="-${BRANCH_NAME}" sdist
                        deactivate
                        '''
                    }
                }
                stage ('Wheel') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python setup.py egg_info --tag-build="-${BRANCH_NAME}" bdist_wheel
                        deactivate
                        '''
                    }
                }
                stage ('Egg') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python setup.py egg_info --tag-build="-${BRANCH_NAME}" bdist_egg
                        deactivate
                        '''
                    }
                }
            }
        }
        stage ('Create Artifacts') {
            environment {
                PROJECT_VERSION = sh (script: 'python setup.py --version', returnStdout: true).trim()
            }
            steps {
                sh '''
                if [[ -d "${WORKSPACE}/docs/build/html/" ]]; then
                    cd "${WORKSPACE}/docs/build/html/"
                    tar -vczf "${WORKSPACE}/${REPOSITORY_NAME}-${BRANCH_NAME}-${PROJECT_VERSION}-${BUILD_NUMBER}.tar.gz" *
                fi
                '''
            }
        }
        stage ('Manage Artifacts') {
            parallel {
                stage ('Archive Artifacts - Packages') {
                    steps {
                        archiveArtifacts artifacts: 'dist/*'
                    }
                }
                stage ('Archive Artifacts - Tarball') {
                    steps {
                        archiveArtifacts artifacts: '*.gz ',
                        onlyIfSuccessful: true
                    }
                }
                /*stage ('Archive Artifacts - pdf') {
                    steps {
                        archiveArtifacts artifacts: 'docs/build/latex/*.pdf',
                        onlyIfSuccessful: true
                    }
                }*/
                stage ('Archive Test Results') {
                    steps {
                        junit allowEmptyResults: true, testResults: 'build/labelx_test_results.xml'
                    }
                }
                stage ('Publish to Test') {
                    when {
                        branch 'dev'
                    }
                    steps {
                        sh '''
                        DST="/var/www/html/staging/docs/${REPOSITORY_NAME}"
                        SRC="docs/build/html/*"
                        if [[ -d "${DST}" ]]; then
                            sudo cp -r $SRC $DST
                        else
                            sudo mkdir -p $DST
                            sudo cp -r $SRC $DST
                        fi
                        '''
                    }
                }
            }
        }
    }
}
