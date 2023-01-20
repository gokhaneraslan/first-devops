pipeline{

    agent any

    stages{

        stage('build'){

            steps{

                script{
                    sh ('docker build -t first_step .')
                }
            }
        }

        stage('run'){

            steps{

                script{

                    sh ('docker run first_step')
                }
            }
        }
    }
}