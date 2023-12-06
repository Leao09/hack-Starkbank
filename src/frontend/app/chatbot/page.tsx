"use client";
import React, { KeyboardEvent, ChangeEvent, useState } from 'react';
import Link from 'next/link';
import styles from '../styles/chatbot.module.css';
import '../globals.css';

const ChatbotPage = () => {

  const [inputText, setInputText] = useState('');

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handleSendClick = () => {
    console.log(inputText)
    setInputText('');
  };

  const handleKeyPress = (event: KeyboardEvent) => {
    if (event.key === 'Enter') {
      handleSendClick();
    }
  };

  const handleMicrophoneClick = () => {
    console.log('microphone click')
  }


  return (
    <div className={styles.container}>
      
      <Link href="/instructions">
        <button type="button" className={styles.backIcon}>
          <img src="/arrow-left.png" alt="back"/> 
        </button>
      </Link>
      


      <div className={styles.instructionsContainer}>

        <button type="button" className={styles.volumeIcon}>
          <img src="/volume-high.svg" alt="volume"/> 
        </button>

        <div className={styles.robotBlueIcon}>
          <img src='/blue-robot.png' alt='blue_robot'/>
        </div>

        <p className={styles.textoInserido}></p>

        <div className={styles.inputWithIcon}>
          <input type="text" placeholder="Digite algo..." className={styles.input} value={inputText} onChange={handleInputChange} onKeyDown={handleKeyPress}/>
          <button className={styles.sendIcon} onClick={handleSendClick}>
              <img src="/send.png" alt="send"/> 
          </button>

          <button onClick={handleMicrophoneClick} className={styles.microphoneIcon}>
              <img src="/microphone-2.svg" alt="microfone"/> 
          </button>
        </div>
        
      </div>
    </div>
  );
}

export default ChatbotPage;
