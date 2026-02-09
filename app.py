import streamlit as st
import pandas as pd
import pickle

# Load model dan daftar kolom hasil training
model = pickle.load(open('model_rf.pkl', 'rb'))
train_cols = pickle.load(open('training_columns.pkl', 'rb'))  # Daftar kolom hasil dummies saat training
# Sangat disarankan menyimpan list kolom hasil dummies agar input sinkron
# training_columns = pickle.load(open('training_columns.pkl', 'rb')) 

st.set_page_config(page_title="Prediksi Vaksin Influenza", layout="centered")

st.title("Aplikasi Prediksi Penerimaan Vaksin Influenza")
st.write("Silakan isi data di bawah ini untuk memprediksi kecenderungan individu dalam menerima vaksin.")

# Membuat form input
with st.form("input_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        h1n1_concern = st.selectbox("Tingkat Kekhawatiran H1N1 (0-3)", [0, 1, 2, 3])
        h1n1_knowledge = st.selectbox("Tingkat Pengetahuan H1N1 (0-2)", [0, 1, 2])
        doctor_recc_h1n1 = st.radio("Rekomendasi Dokter H1N1", [0, 1], format_func=lambda x: "Ya" if x==1 else "Tidak")
        health_worker = st.radio("Tenaga Kesehatan", [0, 1], format_func=lambda x: "Ya" if x==1 else "Tidak")

    with col2:
        opinion_h1n1_vacc_effective = st.slider("Efektivitas Vaksin (1-5)", 1, 5, 3)
        opinion_h1n1_risk = st.slider("Risiko Tanpa Vaksin (1-5)", 1, 5, 3)
        age_group = st.selectbox("Rentang Usia", ["18 - 34 Years", "35 - 44 Years", "45 - 54 Years", "55 - 64 Years", "65+ Years"])
    
    submitted = st.form_submit_button("Lakukan Prediksi")

if submitted:
    raw_input = {
        'h1n1_concern': h1n1_concern,
        'h1n1_knowledge': h1n1_knowledge,
        'doctor_recc_h1n1': doctor_recc_h1n1,
        'health_worker': health_worker,
        'opinion_h1n1_vacc_effective': opinion_h1n1_vacc_effective,
        'opinion_h1n1_risk': opinion_h1n1_risk,
        'age_group': age_group
    }
    
    df_input = pd.DataFrame([raw_input])
    
    # Gunakan get_dummies
    df_input_final = pd.get_dummies(df_input)

    # PERBAIKAN: Paksa nama kolom agar sesuai dengan format training (menggunakan underscore)
    # Contoh: 'age_group_18 - 34 Years' diubah menjadi 'age_group_18_-_34_years'
    df_input_final.columns = [col.replace(" ", "_").lower() for col in df_input_final.columns]

    # Pastikan semua 40 kolom ada (jika ada yang hilang, isi dengan 0)
    # Anda harus memiliki daftar kolom dari saat training, misalnya 'train_cols'
    for col in train_cols:
        if col not in df_input_final.columns:
            df_input_final[col] = 0
            
    # Urutkan kolom sesuai urutan saat training
    df_input_final = df_input_final[train_cols]
    
    prediction = model.predict(df_input_final)
    
    st.subheader("Hasil Analisis:")
    if prediction[0] == 1:
        st.success("Responden diprediksi akan menerima vaksin influenza.")
    else:
        st.warning("Responden diprediksi TIDAK akan menerima vaksin influenza.")