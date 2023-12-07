"use client";
import React, { KeyboardEvent, ChangeEvent, useState, useRef, useEffect } from 'react';
import Link from 'next/link';
import styles from '../styles/chatbotModal.module.css';
import axios from 'axios';
import '../globals.css';


declare global {
  interface Window {
    webkitSpeechRecognition: any;
  }
}

interface Message {
  message: string;
  sender: 'user' | 'bot';
}

interface ModalProps {
 onClose: () => void;
 }

 const ChatbotModal: React.FC<ModalProps> = ({ onClose }) => {

  const [inputText, setInputText] = useState('');
  const [isRecording, setIsRecording] = useState(false);
  const [messageHistory, setMessageHistory] = useState<Message[]>([]);
  const recognitionRef = useRef<any>(null);
  const [audioUrl, setAudioUrl] = useState('/speech.mp3');

  const refreshAudio = () => {
    const newAudioUrl = `/speech.mp3?timestamp=${new Date().getTime()}`;
    setAudioUrl(newAudioUrl);
  };

  useEffect(() => {
    refreshAudio();
  }, []);

  useEffect(() => {
    const messagesContainer = document.querySelector("." + styles.messagesContainer);
    if (messagesContainer) {
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
  }, [messageHistory]);
  
  const onCloseButton = () => {
   console.log("Botão clicado");
   onClose();
  };

  const addToMessageHistory = (message: string, sender: 'user' | 'bot') => {
    setMessageHistory(prevHistory => [...prevHistory, { message, sender }]);
  };

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handleSendClick = async () => {
    if (inputText) {
      addToMessageHistory(inputText, 'user');
      try {
        const response = await axios.post('http://localhost:8000/tts/', { text: inputText });
        if (response.data) {
          addToMessageHistory('Ele está no corredor 3', 'bot');
          refreshAudio();
        }
      } catch (error) {
        console.error('Erro ao enviar texto para TTS:', error);
      }
    }
    setInputText('');
  };

  const handleKeyPress = (event: KeyboardEvent) => {
    if (event.key === 'Enter') {
      handleSendClick();
    }
  };

  const startRecording = () => {
    setIsRecording(true);
    recognitionRef.current = new window.webkitSpeechRecognition();
    recognitionRef.current.continuous = true;
    recognitionRef.current.interimResults = true;

    recognitionRef.current.onresult = (event:any) => {
      const lastResult = event.results[event.results.length - 1];
      const transcribedText = lastResult[0].transcript;
      setInputText(transcribedText);
    };

    recognitionRef.current.start();
  };

  const stopRecording = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
      setIsRecording(false);
    }
  };

  useEffect(() => {
    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.stop();
      }
    };
  }, []);

  const handleMicrophoneClick = () => {
    if (!isRecording) {
      startRecording();
    } else {
      stopRecording();
    }
  };

  return (
    <>
      <div className={styles.backdrop}> </div>
      <div className={styles.modal}>
        <div className={styles.container}>
          <div className={styles.containerModalSaida}>
            <button onClick={onCloseButton} type="button" className={styles.backIcon}>
              <img src="/arrow-left.png" alt="back"/> 
            </button>
            
            <div className={styles.robotBlueIcon}>
                <img src='/blue-robot.png' alt='blue_robot'/>
            </div>
          </div>
          
          <div className={styles.instructionsContainer}>
            <div className={styles.teste}>
              <p className={styles.textoInserido}></p>
              <button type="button" className={styles.volumeIcon}>
                <audio controls src={audioUrl} />
              </button>
            </div>

            <div className={styles.messagesContainer}>
              {messageHistory.map((msg, index) => (
                <div
                  key={index}
                  className={`${styles.message} ${msg.sender === 'user' ? styles.userMessage : styles.botMessage}`}
                >
                  {msg.message}
                </div>
              ))}
            </div>

            <div className={styles.inputWithIcon}>
              <input type="text" placeholder="Digite algo..." className={styles.input} value={inputText} onChange={handleInputChange} onKeyDown={handleKeyPress}/>
              <button className={styles.sendIcon} onClick={handleSendClick}>
                  <img src="/send.png" alt="send"/> 
              </button>

              <button onClick={handleMicrophoneClick} className={styles.microphoneIcon}>
                  {isRecording ? <img src="/stop.png" alt="parar"/> : <img src="/microphone-2.svg" alt="microfone"/> }
              </button>
            </div>
            
          </div>
        </div>
      </div>
    </>
  );
}

export default ChatbotModal;
