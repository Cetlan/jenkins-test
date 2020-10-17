pipeline {
    agent none
    stages {
        stage("Multisystem Pipeline") {
            matrix {
                agent any
                axes {
                    axis {
                        name 'PYTHON'
                        values 'python2.7.12', 'python3.6'
                    }
                }
                stages {
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
                    stage("Check Coverage") {
                        steps {
                            withPythonEnv("System-CPython-2.7") {
                                sh 'coverage xml'
                            }
                            publishCoverage adapters: [coberturaAdapter('**/coverage.xml')], calculateDiffForChangeRequests: true, failBuildIfCoverageDecreasedInChangeRequest: true, failNoReports: true, failUnstable: true, globalThresholds: [[failUnhealthy: true, thresholdTarget: 'Aggregated Report', unstableThreshold: 86.0]], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
                        }
                    }
                }
            }
        }
    }
}
