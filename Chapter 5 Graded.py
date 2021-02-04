#Lee Lacey
#COSC 1315
#08/09/20
#Chapter 5 Forensics


def main():
    
    #Initial Variables
    medullaDiameter = 0.0
    entireHair=0.0
           
    #Inputs for Hair Analysis and Display for User
    print('\nHair Analysis')
    medullaDiameter=float(input('Enter medulla diameter in milliters'))
    entireHair=float(input('Enter Entire hair diameter in milliters'))

    #Call for getHairType      
    getHairType(medullaDiameter,entireHair)

    #Input for Height Analysis and Display for User
    print('Height Analysis\n')
    gender =int(input('Please enter the gender (0 for male 1 for female): '))
        
    #Call for getHeight
    getHeight(gender)
    
#parameters medulla and hair
def getHairType(medulla, hair):    
    
    #Need Ratio of medulla to hair 
    result= medulla/hair
    #Boolean Statement for Animal and Human Hair Comparison
    if result>=0.5:
        print ('The sample provided is from an animal')
        return 0
    else:
        print ('The sample provided is from a human\n')
        return 1
    
#parameter sex of individual
def getHeight(sex):
    #Input for femurHeight  
    femurHeight = float(input('Please enter femur length in cm: '))
    
    #Boolean Statement for Height Calculation based on Gender
    if sex==0:
        height=69.089+2.238*(femurHeight)
        print ('The individual is ',height,'tall.')
    else:
        height=61.412+2.317*(femurHeight)
        print ('The individual is ',height,'tall.')
           
main()
