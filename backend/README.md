# run database docker
 b1: sudo docker pull mongo
 b2: sudo docker run -d -p 27017:27017 --name db mongo
                                               
# run backend without docker
 b1: python3 -m venv venv
 b2: source venv/bin/activate
 b3: pip install -r requirements.txt
 b4: flask run

 
 Lưu ý: Trước khi chạy cần cài docker, python, pip
