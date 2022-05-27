pipeline {
    agent none
    stages{
        stage('Install requirements'){
            agent{
                docker{
                    image 'python:3.6'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
                    sh 'python -m pip install django==2.1.15'
                    sh 'python -m pip install --upgrade pip'
                    sh 'python -m pip install -r requirements.txt'
                    sh 'python -m pip install djongo'
                }
            }
        }
        stage('Compile'){
            agent{
                docker{
                    image 'python:3.6'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
                    sh 'python -m py_compile manage.py'
                    sh 'pip install django_jenkins'
                }
            }
        }
        stage('Tests'){            
            agent{
                docker{
                    image 'python:3.6'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
                     dir("src"){
                        sh 'python manage.py test'
                     }
                }
            }
        }
    }
}
