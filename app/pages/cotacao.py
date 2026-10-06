import streamlit as st

from app.services.cotacao_api import MOEDAS, get_cotacao


st.set_page_config(
    page_title="Cotação de Moedas",
    page_icon="💱",
    layout="centered",
)

st.title("💱 Cotação de Moedas")
st.write("Consulte o valor atual de moedas e criptomoedas em reais.")


@st.cache_data(ttl=30, show_spinner=False)
def consultar(par: str) -> dict:
    # cache de 30s para não bater na API a cada clique
    return get_cotacao(par)


par = st.selectbox(
    "Escolha a moeda:",
    options=list(MOEDAS),
    format_func=lambda p: f"{p} — {MOEDAS[p]}",
)

if st.button("Consultar cotação"):
    try:
        with st.spinner("Consultando..."):
            st.session_state["cotacao"] = consultar(par)
            st.session_state["par"] = par
    except Exception as error:
        st.session_state.pop("cotacao", None)
        st.error(f"Não foi possível consultar a cotação: {error}")

dados = st.session_state.get("cotacao")

if dados:
    par_atual = st.session_state["par"]
    moeda = par_atual.split("-")[0]

    st.success(f"Cotação encontrada para {MOEDAS[par_atual]}.")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Compra (bid)",
            f"R$ {float(dados['bid']):,.2f}",
            delta=f"{float(dados['pctChange']):.2f}%",
        )
    with col2:
        st.metric("Venda (ask)", f"R$ {float(dados['ask']):,.2f}")

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Máxima do dia", f"R$ {float(dados['high']):,.2f}")
    with col4:
        st.metric("Mínima do dia", f"R$ {float(dados['low']):,.2f}")

    st.caption(f"Atualizado em: {dados['create_date']}")

    st.divider()
    st.subheader("Conversor")

    sentido = st.radio(
        "Converter:",
        [f"{moeda} → BRL", f"BRL → {moeda}"],
        horizontal=True,
    )
    valor = st.number_input("Valor:", min_value=0.0, value=1.0, step=1.0)
    bid = float(dados["bid"])

    if sentido.startswith(moeda):
        st.write(f"**{valor:,.4f} {moeda} = R$ {valor * bid:,.2f}**")
    else:
        st.write(f"**R$ {valor:,.2f} = {valor / bid:,.6f} {moeda}**")