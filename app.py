import streamlit as st
import pandas as pd
import pickle


with open('best_model_rf.pkl', 'rb') as f:
    model = pickle.load(f)
with open('training_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)


st.set_page_config(page_title="Prediksi Vaksin Influenza", layout="wide")
st.title("Sistem Penerimaan Vaksin Influenza")
st.write("Silakan isi formulir di bawah ini. Semua pilihan menggunakan bahasa yang mudah dipahami.")
st.markdown("---")
def convert_to_binary(val):
    return 1 if val in ["Ya", "Sudah", "Pernah"] else 0
opini_mapping = {
    "Sangat Rendah": 1,
    "Rendah": 2,
    "Rata-rata": 3,
    "Tinggi": 4,
    "Sangat Tinggi": 5
}
opini_options = list(opini_mapping.keys())
concern_labels = {0: "Tidak Khawatir Sama Sekali", 1: "Sedikit Khawatir", 2: "Cukup Khawatir", 3: "Sangat Khawatir"}
knowledge_labels = {0: "Tidak Tahu Sama Sekali", 1: "Tahu Sedikit", 2: "Sangat Tahu"}
with st.form("main_form"):
    
    st.subheader("Informasi Dasar")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        user_age = st.number_input("Berapa usia Anda saat ini?", min_value=1, max_value=110, value=25)
        # seasonal_vaccine_raw = st.radio("Apakah Anda sudah menerima vaksin flu musiman?", ["Belum", "Sudah"], horizontal=True)
    with col_b:
        health_worker_raw = st.selectbox("Bekerja di bidang kesehatan?", ["Tidak", "Ya"])
        # health_ins_raw = st.radio("Memiliki asuransi kesehatan?", ["Tidak", "Ya"], horizontal=True)
    with col_c:
        doc_h1n1_raw = st.selectbox("Saran dokter untuk vaksin influenza?", ["Tidak", "Ya"])
        # doc_seas_raw = st.radio("Saran dokter untuk vaksin Musiman?", ["Tidak", "Ya"], horizontal=True)

    st.markdown("---")
    st.subheader("Kebiasaan & Kondisi Medis")
    col_d, col_e, col_f = st.columns(3)
    with col_d:
        face_mask_raw = st.selectbox("Sering memakai masker?", ["Tidak", "Ya"])
        wash_hands_raw = st.selectbox("Rajin mencuci tangan?", ["Tidak", "Ya"])
        antiviral_raw = st.selectbox("Mengonsumsi obat-obatan?", ["Tidak", "Ya"])
    with col_e:
        avoidance_raw = st.selectbox("Menghindari kerumunan?", ["Tidak", "Ya"])
        large_gatherings_raw = st.selectbox("Menghindari acara besar?", ["Tidak", "Ya"])
        touch_face_raw = st.selectbox("Sering menyentuh wajah?", ["Tidak", "Ya"])
    with col_f:
        outside_home_raw = st.selectbox("Membatasi keluar rumah?", ["Tidak", "Ya"])
        child_under_6_raw = st.selectbox("Melakukan kontak dengan bayi dibawah 6 bulan?", ["Tidak", "Ya"])
        chronic_med_raw = st.selectbox("Memiliki penyakit kronis?", ["Tidak", "Ya"])

    st.markdown("---")
    st.subheader("Pandangan Anda terhadap Vaksin")
    col_g, col_h = st.columns(2)
    
    with col_g:
        h1n1_concern_raw = st.selectbox("Seberapa khawatir Anda terhadap virus influenza ?", options=list(concern_labels.values()), index=1)
        h1n1_knowledge_raw = st.selectbox("Seberapa tahu Anda tentang virus influenza?", options=list(knowledge_labels.values()), index=1)
        h1n1_eff_raw = st.selectbox("Seberapa efektif vaksin influenza menurut Anda?", options=opini_options, index=2)
        
    with col_h:
        h1n1_risk_raw = st.selectbox("Risiko jatuh sakit jika tidak melakukan vaksin influenza?", options=opini_options, index=2)
        h1n1_sick_raw = st.selectbox("Ketakutan sakit karena efek dari vaksin influenza?", options=opini_options, index=2)
    #     st.write("**Tentang Flu Musiman (Seasonal)**")
    #     seas_eff_raw = st.selectbox("Seberapa efektif vaksin flu musiman menurut Anda?", options=opini_options, index=2)
    #     seas_risk_raw = st.selectbox("Risiko jatuh sakit jika TIDAK vaksin musiman?", options=opini_options, index=2)
    #     seas_sick_raw = st.selectbox("Ketakutan sakit karena efek vaksin musiman?", options=opini_options, index=2)

    st.markdown("---")

    # --- BAGIAN 4: INFORMASI RUMAH TANGGA ---
    st.subheader("Informasi Rumah Tangga")
    col_i, col_j = st.columns(2)
    with col_i:
        adults_in_house = st.number_input("Jumlah orang dewasa di rumah (selain Anda):", 0, 10, 1)
    with col_j:
        children_in_house = st.number_input("Jumlah anak-anak di rumah:", 0, 10, 2)

    st.write("")
    submit = st.form_submit_button("PREDIKSI")
if submit:
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)

    # A. Mapping Usia
    if 18 <= user_age <= 34: input_df['age_group_18_-_34_years'] = 1
    elif 35 <= user_age <= 44: input_df['age_group_35_-_44_years'] = 1
    elif 45 <= user_age <= 54: input_df['age_group_45_-_54_years'] = 1
    elif 55 <= user_age <= 64: input_df['age_group_55_-_64_years'] = 1
    elif user_age >= 65: input_df['age_group_65+_years'] = 1
    input_df['h1n1_concern'] = [k for k, v in concern_labels.items() if v == h1n1_concern_raw][0]
    input_df['h1n1_knowledge'] = [k for k, v in knowledge_labels.items() if v == h1n1_knowledge_raw][0]
    input_df['behavioral_antiviral_meds'] = convert_to_binary(antiviral_raw)
    input_df['behavioral_avoidance'] = convert_to_binary(avoidance_raw)
    input_df['behavioral_face_mask'] = convert_to_binary(face_mask_raw)
    input_df['behavioral_wash_hands'] = convert_to_binary(wash_hands_raw)
    input_df['behavioral_large_gatherings'] = convert_to_binary(large_gatherings_raw)
    input_df['behavioral_outside_home'] = convert_to_binary(outside_home_raw)
    input_df['behavioral_touch_face'] = convert_to_binary(touch_face_raw)
    input_df['doctor_recc_h1n1'] = convert_to_binary(doc_h1n1_raw)
    input_df['chronic_med_condition'] = convert_to_binary(chronic_med_raw)
    input_df['child_under_6_months'] = convert_to_binary(child_under_6_raw)
    input_df['health_worker'] = convert_to_binary(health_worker_raw)
    input_df['opinion_h1n1_vacc_effective'] = opini_mapping[h1n1_eff_raw]
    input_df['opinion_h1n1_risk'] = opini_mapping[h1n1_risk_raw]
    input_df['opinion_h1n1_sick_from_vacc'] = opini_mapping[h1n1_sick_raw]
    input_df['household_adults'] = adults_in_house
    input_df['household_children'] = children_in_house
    input_df['doctor_recc_seasonal'] = 1
    input_df['opinion_seas_vacc_effective'] = 3
    input_df['opinion_seas_risk'] = 3
    input_df['opinion_seas_sick_from_vacc'] = 3
    input_df['seasonal_vaccine'] = 1
    input_df = input_df[model_columns]
    prediction = model.predict(input_df)
    prob = model.predict_proba(input_df)[0][1] * 100
    st.markdown("---")
    st.subheader("Hasil Prediksi")
    # c1, c2 = st.columns(2)
    # with c1:
    #     st.metric("Tingkat Kemungkinan", f"{prob:.2f}%")
    #     st.progress(prob/100)
    # with c2:
    #     hasil_teks = "BERSEDIA VAKSIN" if prediction[0] == 1 else "TIDAK BERSEDIA VAKSIN"
    #     st.metric("Keputusan Model", hasil_teks)

    if prediction[0] == 1:
        st.success(f"Individu akan menerima vaksin influenza.")
    else:
        st.error(f"Individu belum akan menerima vaksin influenza.")