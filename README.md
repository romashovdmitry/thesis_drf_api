# How To Run on local machine and use

Download project

<code>git clone https://github.com/romashovdmitry/thesis_drf_api
cd thesis_drf_api</code>

There is a file example.env. You can create your .env file or just change name to .env and pass your comfortable values.

<code>docker compose up
docker ps</code>

Copy container id and put instead of CID

<code>docker exec -t -i CID bash</code>

After entering the container

<code>python3 manage.py createsuperuser</code>

Create username and password.

Open http://127.0.0.1:8000/swagger/ and use api/token endpoint, put your's username and password. Copy access-token, click button "Authorize" and put copied token. Don't forget to write "Bearer " before token in format "Bearer <COPIED_TOKEN>".  

Join API's beauty! Create your own company with a lot of specaialst . . . on localhost. 
