import streamlit as st
from streamlit_option_menu import option_menu
import os
import random

# --- 1. CONFIGURAÇÃO GERAL E ESTILO ---
st.set_page_config(
    page_title="Garagem do Frank",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CORREÇÃO DO GPS (CAMINHOS) ---
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_ASSETS = os.path.join(DIRETORIO_ATUAL, "assets")
PASTA_RADIO = os.path.join(PASTA_ASSETS, "radio")

# CSS Personalizado
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #ff4b4b; font-family: sans-serif; }
    [data-testid="stMetric"] {
        background-color: #262730;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #444;
    }
    .stButton button { border-radius: 20px; font-weight: bold; }
    
    /* Ajuste da imagem da logo */
    [data-testid="stSidebar"] img {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Função para carregar imagens
def carregar_imagem(nome_arquivo):
    caminho = os.path.join(PASTA_ASSETS, nome_arquivo)
    if os.path.exists(caminho):
        return caminho
    return f"https://via.placeholder.com/300x150?text={nome_arquivo}+nao+encontrado"

# --- 2. LÓGICA DO RÁDIO (ALEATÓRIO + AUTOPLAY) ---
if 'radio_index' not in st.session_state:
    st.session_state.radio_index = 0

# Playlist (Procura musica1.mp3 até musica12.mp3)
playlist = []
for i in range(1, 13):
    playlist.append({
        "titulo": f"Faixa da Garagem {i:02d}", 
        "arquivo": f"musica{i}.mp3" 
    })

def pular_faixa():
    # MODO ALEATÓRIO: Sorteia qualquer música da lista
    novo_index = random.randint(0, len(playlist) - 1)
    
    # Tenta não repetir a mesma música (se tiver mais de 1)
    while novo_index == st.session_state.radio_index and len(playlist) > 1:
        novo_index = random.randint(0, len(playlist) - 1)
        
    st.session_state.radio_index = novo_index

def voltar_faixa():
    if st.session_state.radio_index > 0:
        st.session_state.radio_index -= 1
    else:
        st.session_state.radio_index = len(playlist) - 1

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.image(carregar_imagem("logo_frank.png"), use_container_width=True)
    
    st.markdown("### 📲 Siga a Garagem")
    c_y, c_t = st.columns(2)
    with c_y:
        st.link_button("YouTube", "https://youtube.com/@agaragemdofrank?si=zKmWeoILjWwblYOg", type="primary")
    with c_t:
        st.link_button("TikTok", "https://www.tiktok.com/@agaragemdofrank?_r=1&_t=ZS-91uCZD58CqS")

    st.markdown("---")
    
    # Player de Rádio
    with st.container(border=True):
        st.markdown("### 📻 Rádio Garagem")
        faixa = playlist[st.session_state.radio_index]
        
        st.caption(f"Tocando LIL. FRANK")
        
        # Caminho absoluto para achar o arquivo
        caminho_audio = os.path.join(PASTA_RADIO, faixa["arquivo"])
        
        if os.path.exists(caminho_audio):
            # AQUI ESTÁ A MÁGICA: autoplay=True
            st.audio(caminho_audio, format="audio/mp3", start_time=0, autoplay=True)
        else:
            st.warning(f"Não achei: {faixa['arquivo']}")
            
        c1, c2 = st.columns(2)
        c1.button("Voltar", on_click=voltar_faixa, use_container_width=True)
        c2.button("Próxima", on_click=pular_faixa, use_container_width=True)

    st.markdown("---")
    st.caption("Contato Comercial: chama no TIKTOK")

# --- 4. MENU SUPERIOR ---
selected = option_menu(
    menu_title=None,
    options=["Início", "Telefrank 2000", "Frankverso", "Parceiros", "Inscrição"],
    icons=["house", "wrench", "camera-reels", "people", "pencil-square"],
    default_index=0,
    orientation="horizontal",
    styles={"container": {"background-color": "#262730"}, "nav-link-selected": {"background-color": "#ff4b4b"}}
)

# --- 5. PÁGINA INÍCIO ---
if selected == "Início":
    st.title("BEM-VINDO À GARAGEM DO FRANK")
    st.write("Turbinando motores, restaurando histórias!")

    with st.container(border=True):
        c1, c2 = st.columns([2, 1])
        with c1:
            st.subheader("🤝 Apoie nossos Projetos Sociais")
            st.write("Ajude a comprar ferramentas e peças para os projetos da garagem!.")
        with c2:
            st.success("DOAÇÃO VIA PIX")
            with st.expander("🔑 CLIQUE PARA VER A CHAVE PIX"):
                st.code("df31ecaa-aebe-4da0-a012-8b6471e919e6", language="text")
                st.caption("Copie o código acima.")

    st.divider()
    st.subheader("🍿 Maratona: A Saga da Ipanema")
    
    shorts_ipanema = [
        ("Ep 01 - Recebidos Nagazava", "https://www.youtube.com/watch?v=k1W_uXQYhFU"),
        ("Ep 02 - Teto e Alinhamento", "https://www.youtube.com/watch?v=SrbQp3ZjvRI"),
        ("Ep 03 - Desmontando Tudo", "https://www.youtube.com/watch?v=DB5vivJjk1I"),
        ("Ep 04 - Já desmontamos", "https://www.youtube.com/watch?v=45ByI0DDfnQ"),
        ("Ep 05 - Defeitos Capô", "https://www.youtube.com/watch?v=teMaoWSQXaE"),
        ("Ep 06 - Consertando Defeitos", "https://www.youtube.com/watch?v=2bGWAbI_qLo"),
        ("Ep 07 - Tirando Cola", "https://www.youtube.com/watch?v=Bj9cYppd5m8"),
        ("Ep 08 - Wash Primer", "https://www.youtube.com/watch?v=axI5AeHr0YA"),
        ("Ep 09 - Isolamento", "https://www.youtube.com/watch?v=dy8owmeTpBQ"),
        ("Ep 10 - Aplicação Primer", "https://www.youtube.com/watch?v=kZSQE9U12cA"),
        ("Ep 11 - Controle Lixamento", "https://www.youtube.com/watch?v=kMEBiejJeSQ"),
        ("Ep 12 - Tinta Poliéster", "https://www.youtube.com/watch?v=f9f_JZOpUjQ"),
        ("Ep 13 - Finalização Pintura", "https://www.youtube.com/watch?v=4FH3wLXfhAo"),
        ("Ep 14 - Tirando Papel", "https://www.youtube.com/watch?v=gECG-_Hh7UQ"),
        ("Ep 15 - A Entrega (Final)", "https://www.youtube.com/watch?v=gECG-_Hh7UQ"),
        ("Extra - Motivo do Projeto", "https://www.youtube.com/watch?v=gECG-_Hh7UQ"),
        ("Extra - Quanto Gastamos?", "https://www.youtube.com/watch?v=rUM-h_OnaIk"),
    ]
    
    cols = st.columns(4)
    for i, (titulo, link) in enumerate(shorts_ipanema):
        with cols[i % 4]:
            st.video(link)
            st.caption(titulo)

# --- 6. TELEFRANK ---
elif selected == "Telefrank 2000":
    st.title("📺 Telefrank 2000")
    
    videos_tecnicos = [
        ("Troca Câmbio Gol CHT", "https://www.youtube.com/watch?v=lbU2erkgiQs"),
        ("Partida a Frio no Turbo", "https://www.youtube.com/watch?v=kRaGk9expGs"),
        ("Gol Turbo: Suspensão", "https://www.youtube.com/watch?v=oqob1_CAR_0"),
        ("Escapamento Inox no Fera", "https://www.youtube.com/watch?v=EKkKTXMwJeQ"),
        ("Peças Forjadas e Folgas", "https://www.youtube.com/watch?v=sJvVhZnxwuE"),
        ("Tudo sobre Kit Turbo", "https://www.youtube.com/watch?v=VZw-XfclqLk"),
        ("Embreagem e Volante", "https://www.youtube.com/watch?v=STDCVVDgqtA"),
        ("Motor AP do Zero", "https://www.youtube.com/watch?v=5U7-jKe2JTI"),
        ("Eixo Auxiliar Roletado", "https://www.youtube.com/watch?v=BX5rrtrWb4E"),
        ("Cabeçotes (Retífica Silva)", "https://www.youtube.com/watch?v=8scYwsfYSyQ"),
    ]

    c1, c2 = st.columns(2)
    for i, (titulo, link) in enumerate(videos_tecnicos):
        with (c1 if i % 2 == 0 else c2):
            with st.container(border=True):
                st.video(link)
                st.subheader(titulo)

# --- 7. FRANKVERSO ---
elif selected == "Frankverso":
    st.title("📹 Frankverso")
    st.subheader("🔥 Destaque: Caminhonetes Letts Road")
    st.video("https://www.youtube.com/watch?v=tSlqP2pUS3Q")
    st.divider()

    vlogs = [
        ("Clio do Vizinho", "https://www.youtube.com/watch?v=C97W4cCfeFc"),
        ("Moto de Trilha", "https://www.youtube.com/watch?v=esi1b-6MkMM"),
        ("Perrengue das Motos", "https://www.youtube.com/watch?v=pHFJkZRBJ04"),
        ("Chevette Primo Luciano", "https://www.youtube.com/watch?v=vmv2yKcRVTA"),
        ("Partida Escort Turbo", "https://www.youtube.com/watch?v=9lBgV4v6DJQ"),
        ("Encontro Letts Road", "https://www.youtube.com/watch?v=p4R4XjYGzm0"),
        ("Encontro Copa Mall", "https://www.youtube.com/watch?v=SMYYbmSkh7o"),
        ("Arrancada no Hangar", "https://www.youtube.com/watch?v=Ct-xGsAJWdU"),
        ("XR Tornado Motard", "https://www.youtube.com/watch?v=UFfzXlMDUUk"),
        ("Compra do Escort", "https://www.youtube.com/watch?v=qInWVDJ2Z6o"),
        ("Entrega Escort p/ Esposa", "https://www.youtube.com/watch?v=68_DL2uETpg"),
        ("Compra Moto Nova", "https://www.youtube.com/watch?v=_0_yHuwLyrU"),
        ("Turbinando Escondido", "https://www.youtube.com/watch?v=qZOi7V3jg8U"),
    ]

    c1, c2, c3 = st.columns(3)
    cols = [c1, c2, c3]
    for i, (titulo, link) in enumerate(vlogs):
        with cols[i % 3]:
            with st.container(border=True):
                st.video(link)
                st.caption(titulo)

# --- 8. PARCEIROS ---
elif selected == "Parceiros":
    st.title("🤝 Parceiros")
    
    parceiros = [
        {"nome": "Nagazava Tintas", "desc": "Pintura automotiva.", "cupom": "FRANK15", "link": "https://wa.me/554198442305", "img": "nagazava.png", "tipo": "Zap"},
        {"nome": "Malaguty Bikes", "desc": "Bicicletas.", "cupom": "FRANK10", "link": "https://wa.me/554130538471", "img": "malaguty.png", "tipo": "Zap"},
        {"nome": "Gold Lyon Pneus", "desc": "Pneus e Rodas.", "cupom": "Parceiro Ouro", "link": "https://instagram.com/goldlyonpneus", "img": "goldlyon.png", "tipo": "Insta"},
        {"nome": "Retífica Silva", "desc": "Cabeçotes.", "cupom": "Serviço Top", "link": "https://wa.me/554187792090", "img": "silva.png", "tipo": "Zap"},
        {"nome": "Fera Escapamentos", "desc": "Escapes Inox.", "cupom": "Melhor Ronco", "link": "https://wa.me/554192154371", "img": "fera.png", "tipo": "Zap"},
    ]

    for p in parceiros:
        with st.container(border=True):
            c_img, c_txt, c_btn = st.columns([1, 2, 1])
            with c_img:
                st.image(carregar_imagem(p["img"]), use_container_width=True)
            with c_txt:
                st.subheader(p["nome"])
                st.write(p["desc"])
                st.success(f"🎟️ {p['cupom']}")
            with c_btn:
                st.write("")
                label = "📲 Zap" if p["tipo"] == "Zap" else "📸 Insta"
                st.link_button(label, p["link"], type="primary")

# --- 9. INSCRIÇÃO ---
elif selected == "Inscrição":
    st.title("📝 Inscreva seu Projeto")
    with st.form("ficha"):
        st.text_input("Nome Completo")
        st.text_input("WhatsApp")
        st.text_input("Carro/Moto e Ano")
        st.text_area("História e porque devemos escolher seu projeto")
        if st.form_submit_button("ENVIAR"):
            st.balloons()
            st.success("Recebido!")