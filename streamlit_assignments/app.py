import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Price Visualization" ,layout="wide")

st.title("📈 Stock Analysis Dashboard")
st.subheader("Stock Visualization & News Summarization")

st.sidebar.header("Controls")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol","AAPL")
print(stock_symbol)
period = st.sidebar.selectbox("Enter ime period",["1mo","3mo","6mo","1y","5y"])

stock_data = yf.download(stock_symbol,period=period)
print(stock_data)
# st.write(f"stock data : {stock_data}")

st.subheader(f"Stock Price for {stock_symbol}")

if not stock_data.empty :
    st.line_chart(stock_data["Close"])
else:
    st.error("Invalid Stock Symbol")

st.subheader("📰 Stock News Summarization ")

user_text = st.text_area("Paste Stock Related News or Report Here :",height=200)
from transformers import pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization",model="facebook/bart-large-cnn")
summarizer = load_summarizer()

def truncate_text(text, max_words=500):
    words = text.split()
    if len(words) > max_words:
        return " ".join(words[:max_words])
    return text

if st.button("Summarize"):
    if user_text.strip() == "":
        st.warning("Please enter text to summarize")
    else:
        safe_text = truncate_text(user_text)

        with st.spinner("Summarizing..."):
            summary = summarizer(
                safe_text,
                max_length=120,
                min_length=40,
                do_sample=False
            )

        st.success("Summary:")
        st.write(summary[0]["summary_text"])
