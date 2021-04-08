server {
        listen 80;
        listen [::]:80;

        root /var/www/sit.myvnc.com/html;
        index index.html index.htm index.nginx-debian.html;

        server_name sit.myvnc.com www.sit.myvnc.com;

        location / {
                try_files $uri $uri/ =404;
        }
}

