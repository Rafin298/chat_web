## Getting Started
1. Activate the virtual environment
   
    ```
    #using git bash
    git clone repository
    cd CarelogixChat
    python -m venv env
    source env/Scripts/activate
    ```
2. Install the requirements
    ```
    pip install -r requirements.txt
    ```
    
3. migrate
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
4. runserver
    ```
    python manage.py runserver
    ```
5. Signup and Login  
    Sample signup :  
    name : Rafin  
    Password : a1234b567 

6. go to zones and create e new zone and start chatting  

## Learn More
ChatWEB is a Django application designed for group discussions in real-time. It leverages Django Channels to provide a seamless chatting experience within designated chat zones.
Video Demo of APP : https://drive.google.com/file/d/1Cd8x34rWHnNNEdScI0NWHqLgKAwCVOUx/view?usp=sharing
