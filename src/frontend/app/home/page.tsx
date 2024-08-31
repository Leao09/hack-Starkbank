"use client";
import Navbar from '../components/navbar';
import Icon from '../components/icon';
import User from '../components/user';
import '../globals.css';
import styles from '../styles/Home.module.css';
import React, { useState, useEffect  } from 'react';
import Modal from '../components/modal';
import Link from 'next/link';
import ChatbotModal from '../components/chatbotModal';


export default function Home() {

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isChatbotModalOpen, setIsChatbotModalOpen] = useState(false);
  
  const handleOpenModal = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const handleOpenChatbotModal = () => {
    setIsChatbotModalOpen(true);
  };

  const handleCloseChatbotModal = () => {
    setIsChatbotModalOpen(false);
  };
    return (
      <>
        <Navbar />
        <User />
        <div className={styles.homeContent}>
          <div className={styles.columns}>
            
            <div className={styles.textSection}>
              <p className={styles.title}>Bem vindo a home!</p>
              <p className={styles.subtitle}>Aqui você poderá fazer uma nova requisição ou consultar uma peça do almoxarifado</p>
            </div>

            <div className={styles.imageSection}>
              <img src="/peopleTalk.png" alt="Pessoas conversando" className={styles.contentImage} />
            </div>

          </div>

          <div className={styles.buttons}>
            <button className={styles.blueButton} onClick={handleOpenModal}>Nova Requisição</button>
            {isModalOpen && <Modal onClose={handleCloseModal} />}
            <Link href="/search">
              <button className={styles.blueButton}>Busca de Peças</button>
            </Link>
          </div>
        </div>
        <button onClick={handleOpenChatbotModal}>
          <Icon />
        </button>
        {isChatbotModalOpen && <ChatbotModal onClose={handleCloseChatbotModal} />}
      </>
    );
  }