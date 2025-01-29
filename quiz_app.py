import streamlit as st

def main():
    st.title("Malware Threats Quiz")
    st.markdown("Test your knowledge of malware types, components, and propagation methods.")

    questions = [
        {
            "question": "What is the primary purpose of ransomware?",
            "options": [
                "Monitor user activity",
                "Encrypt data and demand payment for decryption",
                "Spread through removable media"
            ],
            "answer": "Encrypt data and demand payment for decryption",
            "explanation": "Ransomware blocks access to data until a ransom is paid."
        },
        {
            "question": "Which malware component conceals malware to prevent reverse engineering?",
            "options": ["Dropper", "Crypter", "Downloader"],
            "answer": "Crypter",
            "explanation": "Crypters encrypt malware to evade detection and analysis."
        },
        {
            "question": "How does malware commonly spread via USB devices?",
            "options": ["Phishing emails", "Removable media", "Social engineering"],
            "answer": "Removable media",
            "explanation": "Infected USB drives propagate malware like Stuxnet."
        },
        {
            "question": "Which type of malware primarily tracks browsing activity to display targeted ads?",
            "options": ["Spyware", "Adware", "Trojan"],
            "answer": "Adware",
            "explanation": "Adware collects browsing data to serve personalized advertisements."
        },
        {
            "question": "True or False: Fileless malware leaves no traces on the file system.",
            "options": ["True", "False"],
            "answer": "True",
            "explanation": "Fileless malware operates in memory, avoiding file-based detection."
        },
        {
            "question": "What best describes a Trojan horse?",
            "options": [
                 "Self-replicates across networks",
                "Disguises as legitimate software",
                "Encrypts user files"
            ],
            "answer": "Disguises as legitimate software",
            "explanation": "Trojans mimic trusted software to trick users into execution."
         },
        {
            "question": "Which tool is an example of a dropper used for malware deployment?",
            "options": ["Emotet", "Wireshark", "Nmap"],
            "answer": "Emotet",
            "explanation": "Emotet is a notorious dropper for deploying malware payloads."
        },
        {
             "question": "What best describes a botnet?",
            "options": [
                "Encrypted files",
                "A network of compromised computers",
                "Phishing emails"
             ],
            "answer": "A network of compromised computers",
             "explanation": "Botnets are networks of infected devices controlled by attackers."
         },
         {
            "question": "Which type of malware often uses email attachments to deliver its payload?",
            "options": ["Worm", "Ransomware", "Trojan"],
            "answer": "Trojan",
            "explanation":"Trojans often use email attachments to trick users into opening infected files."
         },
        {
            "question":"What is the purpose of a 'rootkit'?",
            "options":[
              "To scan for vulnerabilities",
               "To hide the presence of malware",
               "To encrypt data"
            ],
            "answer":"To hide the presence of malware",
            "explanation":"Rootkits hide malicious activity and presence of malware"
        },
        {
            "question":"Which type of malware propagates itself across networks without user interaction?",
            "options":[
              "Worm",
               "Virus",
              "Spyware"
            ],
            "answer":"Worm",
            "explanation":"Worms can automatically spread across networks without user interaction."
        }
    ]
    
    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        selected = st.radio("Choose an answer:", q["options"], key=f"q{i}", index=None)
        
        if st.button("Check Answer", key=f"btn{i}"):
            if selected == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. Correct answer: {q['answer']}")
            with st.expander("Explanation"):
                st.write(q["explanation"])
            st.write("---")

    st.header("Results")
    st.write(f"Final Score: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()