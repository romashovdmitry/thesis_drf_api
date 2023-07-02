# How To Run on local machine and use

Download project

<code>git clone https://github.com/romashovdmitry/thesis_drf_api
cd thesis_drf_api</code>

There is a file example.env. You can create your .env file or just change name to .env and pass your comfortable values.

<code>docker compose up</code>

To work with Employee model, authentication by JWT is required. Open http://127.0.0.1:8000/swagger/ and use api/token endpoint. Copy access-token, click button "Authorize" and put copied token. Don't forget to write "Bearer " before token in format "Bearer <COPIED_TOKEN>".  

Also, you can use browsarble DRF API on localhost. 
