# save this as app.py
from flask import Flask, request, escape, render_template, abort
import pickle
 

app = Flask(__name__)
model = pickle.load(open('model07.sav','rb'))

@app.route('/')
def home():
    prediction= ''
    return render_template("prediction.html", **locals())

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    gender = request.form['gender']
    #if request.method == 'POST':
    married = request.form['married']
    age = request.form['age']
    graduated = request.form['graduated']
    profession = request.form['profession']
    experience = request.form['experience']
    spending = request.form['spending']
    size = request.form['size']
          
        
    #gender
    if(gender == "Male"):
        male=1
    else:
        male=0
        
        #married
    if(married == "Yes"):
        married_yes = 1
    else:
        married_yes = 0

    #graduate
    if(graduated == "yes"):
        graduated_yes = 1
    else:
        graduated_yes = 0
        
        #profession
    if(profession == "Doctor"):
        profession_Doctor = 1
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 0   
    elif(profession == "Engineer"):
        profession_Doctor = 0
        profession_Engineer = 1
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 0
    elif(profession == "Entertainment"):
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 1
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 0
    elif(profession == "Executive"):
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 1
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 0
    elif(profession == "Healthcare"):
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 1
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 0
    elif(profession == "Homemaker"):
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 1
        profession_Lawyer = 0
        profession_Marketing = 0        
    elif(profession == "Lawyer"):
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 1
        profession_Marketing = 0
    elif(profession == "Marketing"):
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 1
    else:
        profession_Doctor = 0
        profession_Engineer = 0
        profession_Entertainment = 0
        profession_Executive = 0
        profession_Healthcare = 0
        profession_Homemaker = 0
        profession_Lawyer = 0
        profession_Marketing = 0
        
        #spending score
    if(spending == "High"):
        spending_High = 1
        spending_Low = 0
    elif(spending == "Low"):
        spending_High = 0
        spending_Low = 1
    else:
        spending_High = 0
        spending_Low = 0
        
        #age
    if(age == "30-40"):
        age_30 = 1
        age_40 = 0
        age_50 = 0
        age_60 = 0
    elif(age == "40-50"):
        age_30 = 0
        age_40 = 1
        age_50 = 0
        age_60 = 0
    elif(age == "50-60"):
        age_30 = 0
        age_40 = 0
        age_50 = 1
        age_60 = 0
    elif(age == "60+"):
        age_30 = 0
        age_40 = 0
        age_50 = 0
        age_60 = 1
    else:
        age_30 = 0
        age_40 = 0
        age_50 = 0
        age_60 = 0
        
        #experience
    if(experience == "5-10"):
        experience_5 = 1
        experience_10 = 0
    elif(experience == "10+"):
        experience_5 = 0
        experience_10 = 1
    else:
        experience_5 = 0
        experience_10 = 0
        
        #family size
    if(size == "3-6"):
        size_3 = 1
        size_6 = 0
    elif(size == "6+"):
        size_3 = 0
        size_6 = 1
    else:
        size_3 = 0
        size_6 = 0
        
        # #segmentation status
        # if(segment == "A"):
        #     segment_new = 0
        # elif(segment == "B"):
        #     segment_new = 1
        # elif(segment == "C"):
        #     segment_new = 2
        # else:
        #     segment_new = 3

    prediction = model.predict([[male, married_yes,graduated_yes, profession_Doctor, profession_Engineer, profession_Entertainment, profession_Executive, profession_Healthcare, profession_Homemaker, profession_Lawyer, profession_Marketing, spending_High, spending_Low, age_30, age_40, age_50, age_60, experience_5, experience_10, size_3, size_6]])[0]

        # print(prediction)
        
        # if(prediction == "A"):
        #     prediction ="A"
        # elif(prediction == "B"):
        #     prediction = "B"
        # elif(prediction == "C"):
        #     prediction = "c"
        # else:
        #     prediction = "D"

    return render_template("prediction.html", **locals())
    



    #  else:
    #     return render_template("prediction.html")
 
if __name__=="__main__":
    app.run(debug=True)

    
 

    