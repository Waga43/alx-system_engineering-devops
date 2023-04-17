# 0x13. Firewall

## Preamble

Some students may encounter problems logging onto their ALX remote server. To get around this follow the below procedure:

1. Open any of your ALX Sandboxes and run the following command:

`ssh-keygen`

Follow the default prompts or modify if you wish. I would advise you go with the defaults.

2. After generating your ssh private and public keys, you can access these keys by opening the following directory:

`ls ~/.ssh` OR `cd ~/.ssh`

You will see the following files listed- `id_rsa` (private ssh key) and `id_rsa.pub` (public ssh key). Copy the contents of the `id_rsa.pub` file.

3. Visit your [ ALX Intranet profile page](https://intranet.alxswe.com/users/my_profile) and paste the copied `id_rsa.pub` key into the **SSH public key** box provided under the *Technical information* section.

4. Go to your [ALX Servers page](https://intranet.alxswe.com/servers) and click on the drop down arrow under **Actions**. Select **Ask a new server** option and wait for the process to complete. Your new server should be up and running in notime.

5. Open your Sandbox from Step 1 above and run the below command:

`ssh -i ~/.ssh/id_rsa username@your_server_ip_address`

In my case, the command is as follows:

`ssh -i ~/.ssh/id_rsa ubuntu@35.153.194.233`

6. You should be logged into your remote server. Subsequently you can exit the remote server using the `exit` command and log back in using the below command:

`ssh username@your_server_ip_address` . For me this is: `ssh ubuntu@35.153.194.233`


_For this project, we expect you to look at this concept:_

- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

![https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

### Your servers without a firewall…

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

## Resources

**Read or watch**:

- [What is a firewall](https://intranet.alxswe.com/rltoken/vjB4LyHRdtEImzZcuD89ZQ "What is a firewall")

`telnet` is a very good tool to check if sockets are open with `telnet IP PORT`.

[How to Setup a Firewall with UFW](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)

[How to Configure a Firewall with UFW on Ubuntu 20.04](https://www.cyberciti.biz/faq/how-to-configure-firewall-with-ufw-on-ubuntu-20-04-lts/)

[UFW Commands](https://serverspace.io/support/help/osnovnye-komandy-ufw/)


## Warning!

**Containers on demand cannot be used for this project (Docker container limitation)**

**Be very careful with firewall rules! For instance, if you ever deny port `22/TCP` and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.**



