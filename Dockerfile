# Käytetään virallista Robot Framework Browser -kuvaa
FROM marketsquare/robotframework-browser:19.12.5

ENV PYTHONDONTWRITEBYTECODE=1

# Vaihdetaan root-käyttäjään oikeuksien korjaamista ja asennuksia varten
USER root

# 1. Poistetaan ubuntu-käyttäjä, jotta UID 1000 vapautuu
RUN userdel -r ubuntu || true \
    && userdel -r node || true

# 2. PAKOTETAAN pwuser käyttämään WSL:n kanssa täsmäävää UID/GID 1000 -tunnusta
RUN usermod -u 1000 pwuser && groupmod -g 1000 pwuser

# 3. Kopioidaan ja asennetaan riippuvuudet väliaikaiskansion kautta
# (Näin vältämme turhan tiedoston roikkumisen varsinaisessa työkansiossa)
COPY requirements.txt /tmp/
RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

# Vaihdetaan lopuksi takaisin turvalliseen pwuser-käyttäjään
USER pwuser