pipeline {
    
    agent any
    
    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage('Checkout source files from GitHub') {
            steps {
                git branch: 'main', 
                    credentialsId: 'github-bt4301', 
                    url: 'https://github.com/tanwk/src.git'
            }
        }

        stage('Set up Python virtual environment') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                
                pip install pytest 
                pip install pytest-html 
                pip install pylint
                pip install pylint-report
                pip install flask
                pip install connexion[flask,swagger-ui,uvicorn]
                '''
            }
        }
        
        stage('Run unit tests') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                python3 -m pytest mymathlibtest.py --html=pytest-mymathlibtest.html --self-contained-html
                '''
            }
        }
        
        stage('Generate lint report') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                python3 -m pylint mymathlib.py --load-plugins=pylint_report --output-format=pylint_report.CustomJsonReporter > lint-report.json || true
                '''
                sh '''
                . ${VENV_DIR}/bin/activate
                python3 ${VENV_DIR}/lib/python3.12/site-packages/pylint_report/pylint_report.py lint-report.json -o lint-report.html
                '''
            }
        }
        
        stage('Start Connexion Flask application') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pkill -f mymathserver.py || true
                sleep 1
                export JENKINS_NODE_COOKIE=dontkillme
                nohup python3 mymathserver.py > mymathserver.log 2>&1 &
                echo $! > mymathserver.pid
                sleep 3
                curl -s http://localhost:5000 || echo "Application may not be running"
                ps -p $(cat mymathserver.pid) || echo "Process not running"
                '''
            }
        }

        stage('Run unit tests for API reliability') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                python3 -m pytest mymathservertest.py --html=pytest-mymathservertest.html --self-contained-html
                '''
            }
        }
    }
}