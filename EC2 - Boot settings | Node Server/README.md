### Running an httpd server at the launch of EC2 instance.

- First, let us launch an EC2 instance. For this we can opt for the free tier AMI i.e. "Amazon Linux 2 AMI (HVM), SSD Volume Type".
- Then we select the "t2.micro" instance type which falls under free tier.
- Under configure instance details, we can let everything be default, except the "Advanced details" tab.
- In the Advanced details -> User Data field, we can provide a shell script that runs at the launch of the instance.
![image](https://user-images.githubusercontent.com/72746084/124359794-244f5d80-dc44-11eb-9d9a-c1172953a6cc.png)
-  Now the httpd server is running on the instance.

### Running a Node server
- We can now run a node server that displays a simple "Hello World!" on the running instance.
- To do so, first install node on Amazon Linux. For reference: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html
- Now create an index.js and run it using node.
![image](https://user-images.githubusercontent.com/72746084/124359970-d71fbb80-dc44-11eb-9873-71285a0fc742.png)
![image](https://user-images.githubusercontent.com/72746084/124359983-ebfc4f00-dc44-11eb-8a1a-f031809b5e0a.png)
![image](https://user-images.githubusercontent.com/72746084/124360006-07675a00-dc45-11eb-8d50-eda5f8ba151a.png)
- Now our node server must be up and running on port 8080.
- Get the public ip address of the instance and navigate to the url "http://<INSTANCE-PUBLIC-IP>:8080".
- It should display "Hello world!".
  ![image](https://user-images.githubusercontent.com/72746084/124360078-64fba680-dc45-11eb-822e-2ba60af3c9ca.png)





