#www.1byteco.com 


The original idea belongs to: https://bokoko33.me/

First time only install dependencies with:
npm i 

Local development server:
npm run dev


Just testing around with TaskCluster and Ci/CD. 
change 1.....testing testing...1...2...3...

day 99 of troubleshooting..
export DEBIAN_FRONTEND=noninteractive && \
apt-get update -y && \
apt-get install -y python3 python3-pip git && \
python3 -m venv /home/worker/venv && \
source /home/worker/venv/bin/activate && \
git clone https://github.com/mobm93/mobm93.github.io.git && \
cd mobm93.github.io && \
pip install -r requirements.txt && \
pytest -s tests/test_home_page.py
