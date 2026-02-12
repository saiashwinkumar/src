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
                    url: 'https://github.com/saiashwinkumar/src.git'
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
              . venv/bin/activate
              python3 -m pytest -q mymathlibtest.py --html=pytest-mymathlibtest.html --self-contained-html
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
                python3 -m pylint_report.pylint_report lint-report.json -o lint-report.html
                '''
            }
        }
        
        stage('Start Connexion Flask application') {
          steps {
            sh '''
              set -e
              . venv/bin/activate
        
              # Use a non-conflicting port (macOS AirTunes often occupies 5000)
              export PORT=5001
              export JENKINS_NODE_COOKIE=dontkillme
        
              # Kill old server if any
              pkill -f mymathserver.py || true
              sleep 1
        
              # Free up port 5001 if anything is using it
              if lsof -ti tcp:$PORT >/dev/null 2>&1; then
                echo "Port $PORT is in use. Killing process..."
                lsof -ti tcp:$PORT | xargs kill -9 || true
                sleep 1
              fi
        
              # Start server in background and capture PID
              nohup python3 mymathserver.py > server.log 2>&1 &
              echo $! > mymathserver.pid
        
              sleep 3
        
              # Show what is responding (headers matter for debugging)
              curl -i http://127.0.0.1:$PORT/ || true
        
              # Fail fast if server died, and print logs
              ps -p $(cat mymathserver.pid) || (echo "Process not running"; echo "=== server.log ==="; tail -200 server.log; exit 1)
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









