import streamlit as st
from streamlit_option_menu import option_menu
import AppLayout


# 2. horizontal menu

def menu_opt(menu_names, icons):
	menu = option_menu(None, menu_names, 
    icons=icons, 
    menu_icon="cast", default_index=1, orientation="horizontal")
	return menu

#st.markdown("""	1. >>oi	1. **tudo bem**	1. __hello__	""")

import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
	al=AppLayout.AppLayout(st)
	cs=al.call_markdown()
	al.styleholder.markdown(cs, unsafe_allow_html=True)
	st.title("ALuBIke App")

	menu_names = ["Home", "Login", "Cadastrar"]
	icons = ['house', 'person', "book"]
	#choice = st.sidebar.selectbox("Menu",menu)
	choice = menu_opt(menu_names, icons)

	if choice == "Home":
		st.subheader("""
			Muito mais que um aluguel, uma transformação em nossa Comunidade!!""")
		st.markdown("""<p style="text-align:justify; line-height: 1,1; fonte-size:10px; color: orange">
			Trazendo uma proposta ousada e desafiadora, propomos o exercício da
		 cidadania através de uma atitude nobre: Pessoas que como eu e você querem um mundo
		  melhor, estão disponibilizando suas bicicletas em prol de melhorar a mobilidade 
		  urbana, pois pessoas que possuem carros podem optar por usar uma bicicleta e ao 
		  mesmo tempo ajudar de forma real as pessoas que precisam de um transporte para seu
		   trabalho e até mesmo seu lazer!!!</p>""", unsafe_allow_html=True)

	elif choice == "Login":
		st.subheader("Escolha aqui sua bicicleta")

		username = st.text_input("Nome do Usuário")
		password = st.text_input("Senha",type='password')
		if st.checkbox("Login"):

			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success(f"Seja bem vindo {username}")
				st.subheader('Escolha o bairro mais próximo a você')

				task = st.selectbox("Bairro: ",["Urca","Copacabana","Leme"])
				if task == "Urca":
					st.markdown(f"Aqui serão mostradas as bicicletas disponíveis na {task}")

				elif task == "Copacabana":
					st.markdown(f"Aqui serão mostradas as bicicletas disponíveis em {task}")

				elif task == "Leme":
					st.markdown(f"Aqui serão mostradas as bicicletas disponíveis no {task}")

			else:
				st.warning("Incorrect Username/Password")





	elif choice == "Cadastrar":
		st.subheader("Cadastrar novo usuário")
		new_user = st.text_input("Nome")
		new_password = st.text_input("Senha",type='password')

		if st.button("Cadastrar"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("Parabéns, você agora está cadastrado")
			st.info("Agora já pode fazer o seu Login")

if __name__ == '__main__':
	main()
