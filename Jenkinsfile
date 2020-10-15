pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
        stage("Setup Virtual Environment") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'pip install coverage'
                }
            }
        }
        stage("Unit Tests") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'coverage run -m unittest discover'
                }
            }
        }
        stage("Code Coverage") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'coverage xml'
                }
                publishCoverage adapters: [istanbulCoberturaAdapter(path: '**/coverage.xml', thresholds: [[failUnhealthy: true, thresholdTarget: 'Line', unhealthyThreshold: 100.0, unstableThreshold: 100.0]])], failNoReports: true, failUnhealthy: true, failUnstable: true, globalThresholds: [[failUnhealthy: true, thresholdTarget: 'Line', unhealthyThreshold: 100.0, unstableThreshold: 100.0]], skipPublishingChecks: true, sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
            }
        }
    }
}
