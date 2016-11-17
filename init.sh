
sudo rm /etc/nginx/sites-enabled/*
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo rm  /etc/gunicorn.d/*
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn stop
cd web
gunicorn -w 4 -b 0.0.0.0:8080 hello:app &
