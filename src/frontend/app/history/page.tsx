"use client";
import Navbar from "../components/navbar";
import User from "../components/user";
import Icon from "../components/icon";
import Search from "../components/search";
import Table from "../components/table";
import styles from "../styles/Navigate.module.css";
import Image from "next/image";
import "../globals.css";
import React, { useState } from "react";
import ChatbotModal from "../components/chatbotModal";

export default function History() {
  const [isChatbotModalOpen, setIsChatbotModalOpen] = useState(false);

  const handleOpenChatbotModal = () => {
    setIsChatbotModalOpen(true);
  };

  const handleCloseChatbotModal = () => {
    setIsChatbotModalOpen(false);
  };

  return (
    <>
      <Navbar />
      <div className={styles.userInfo}>
        <Image src="/profile.png" alt="Foto de Perfil" width={80} height={80} />
        <span className={styles.userName}>Usuário X</span>
      </div>
      <div className={styles.mainContainer}>
        <div className={styles.searchBarContainer}>
          <Search />
        </div>
        <div className={styles.tableContainer}>
          <Table />
        </div>
      </div>
      <button onClick={handleOpenChatbotModal}>
        <Icon />
      </button>
      {isChatbotModalOpen && <ChatbotModal onClose={handleCloseChatbotModal} />}
    </>
  );
}
