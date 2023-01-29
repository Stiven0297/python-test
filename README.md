# PropertyApi
- Python
- Gunicorn 
- Mysql-connector
- Pytest
#### RUN DOCKER
`docker-compose build`
`docker-compose up`
<p>Run the docker instance to upload the project</p>

### ENDPOINTS
* Get list of properties 
  * url - `http://127.0.0.1:8000/property`
    * Request body:
      ```
      HTTP GET - http://127.0.0.1:8000/property - JSON REQUEST
    
      {
         "status": "comprando", 
         "city": "bogota", 
         "year": 2000
      }
      ```
    * Response:
        ```
      JSON RESPONSE
    
      [
           {
               "address": "calle 23 #45-67",
               "city": "bogota",
               "price": 120000000,
               "description": "Hermoso apartamento en el centro de la ciudad",
               "status": "comprando"
           }
      ]
      ```
### ARQUITECTURE
<h4>Repository pattern</h4>
<p>This pattern is used in order for the microservice to separate the logic that retrieves the data for its assignment to a model, from the business logic that acts on these models, allowing this logic layer to be more independent of the mapping layer.</p>
<p>
On the other hand, the work unit pattern allows centralizing the connections to the data, serving as a middle layer to achieve a reversal of processed data if a committee is not invoked or if there is some type of inconsistency.</p>

- Diagram: https://drive.google.com/file/d/1ssaP-VJXCvcHOpCNHauKLA0oq-MqEBSv/view?usp=share_link