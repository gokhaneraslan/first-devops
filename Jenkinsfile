pipeline{

    agent any

    stages{

        stage('build'){

            steps{

                script{
                    sh ('sudo docker build -t first_step .')
                }
            }
        }

        stage('run'){

            steps{

                script{

                    sh ('sudo docker run first_step')
                }
            }
        }
    }
}
