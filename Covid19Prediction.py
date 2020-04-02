class Covid19Prediction:
    def __init__(self):
        self.theta_0 = 3.5
        self.theta_1 = 3.5
        self.learning_rate = 0.1
        self.theta_0_funValue = 0
        self.theta_1_funValue = 0
        self.temp_0 = 0
        self.temp_1 = 0
    def costFunctionForTheta_0(self, input_x1, output, theta_0_funValue, theta_0, theta_1):
        print("Inside costFunctionForTheta_0 mtd.")
        for trainingExample in zip(input_x1, output):
            self.theta_0_funValue += (theta_0 + (theta_1 * trainingExample[0]) - trainingExample[1])
        print("Cost value of theta_0"," - ", self.theta_0_funValue)
        return self.theta_0_funValue   

    def costFunctionForTheta_1(self, input_x1, output, theta_1_funValue, theta_0, theta_1):
        print("Inside costFunctionForTheta_1 mtd.")
        for trainingExample in zip(input_x1, output):
            self.theta_1_funValue += (theta_0 + (theta_1 * trainingExample[0]) - trainingExample[1]) *trainingExample[0]
        print("Cost value of theta_1 "," - ", self.theta_1_funValue)
        return self.theta_1_funValue   

    def gradientOptimization(self, input_x1, output, theta_0, theta_1, theta_0_funValue, theta_1_funValue, temp_0, temp_1, user_input):
        print("Started training")
        for iteration in range(20000):
            self.temp_0 = self.theta_0 - (self.learning_rate * ((1.0/len(input_x1)) * self.costFunctionForTheta_0(input_x1, output, self.theta_0_funValue, self.theta_0, self.theta_1)))
            self.temp_1 = self.theta_1 - (self.learning_rate * ((1.0/len(input_x1)) * self.costFunctionForTheta_1(input_x1, output, self.theta_0_funValue, self.theta_0, self.theta_1)))
            self.theta_0 = self.temp_0
            self.theta_1 = self.temp_1
            print("Iteration" ,iteration, "Completed")
        #return [theta_0, theta_1]
        self.hypothesis = self.theta_0 + (self.theta_1 * user_input)
        print("theta_0 = ", self.theta_0, " and theta_1 = ", self.theta_1)
        print("YES THE PREDICTION IS DONE..MY PREDICTION FOR YOUR INPUT", user_input, " IS => ", self.hypothesis)


input_x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] #days count from 2020-03-22 to 2020-03-29 yyyy/mm/dd format
output = [69, 102, 66, 86, 78, 151, 143, 110, 208] #Tamilnadu data on respective input days
"""theta_0 = 1
theta_1 = 0.5
learning_rate = 0.1
theta_0_funValue = 0
theta_1_funValue = 0
temp_0 = 0
temp_1 = 0"""
user_input = input('ENTER THE INPUT BADASSSS : ')
obj = Covid19Prediction()
obj.gradientOptimization(input_x1, output, obj.theta_0, obj.theta_1, obj.theta_0_funValue, obj.theta_1_funValue, obj.temp_0, obj.temp_1, user_input)