
'use client';
import styles from '/app/styles/PrimeiraTela.module.css';
import React, { useState } from 'react';
import Icon from './components/icon';
import ChatbotModal from './components/chatbotModal';
// import HomePage from './metabasePage';
export default function PrimeiraTela() {
  const [isChatbotModalOpen, setIsChatbotModalOpen] = useState(false);
  const handleOpenChatbotModal = () => {
    setIsChatbotModalOpen(true);
  };

  const handleCloseChatbotModal = () => {
    setIsChatbotModalOpen(false);
  };
  return (
    <div className={styles.container}>
      {/* Espaço cinza com texto */}
      <div className={styles.metabaseSection}>
        <h2>Dash do Metabase</h2>
        {/* <HomePage /> o metabase seria chamado aqui */}
      </div>
          <button onClick={handleOpenChatbotModal}>
          <Icon />
        </button>
        {isChatbotModalOpen && <ChatbotModal onClose={handleCloseChatbotModal} />}
    </div>
  );
};
