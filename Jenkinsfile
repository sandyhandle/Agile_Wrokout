pipeline {
	agent any
 	stages {
 		stage("Compile") {
 			steps {
 				echo "no need to build python code"
 			}
 		}
 		stage("Unit test") {
 			steps {
 				sh "python tests.py"
 			}
 		}
 	}
}
