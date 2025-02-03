# FIREWALL
````````
A security system that monitors and controls incoming and outgoing network traffic based
on predetermined security rules

# USES
```````
   1. Network Security – Prevents unauthorized access to sensitive data.
   2. Preventing Cyber Attacks – Blocks threats like DDoS attacks, malware, and hacking attempts.
   3. Access Control – Restricts users from accessing specific sites or applications.
   4. Logging and Monitoring – Tracks traffic patterns for security analysis.
   5. VPN Protection – Encrypts remote connections for secure communication.

# CONFIGURING A FIREWALL ON LINUX
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   sudo ufw allow 22/tcp
   sudo ufw enable

   The above configuration denies all incoming network traffics, allow all outgoing
   and also allow SSH connection at port 22.
