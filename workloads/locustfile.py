from locust import HttpUser, task


class JustAUser(HttpUser):
    
    @task
    def get_user(self):

        response = self.client.get("/users/{}".format())
        
        if response.status_code == 200:
            return response.json()

        return None