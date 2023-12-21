'use client';
import React, { useState, useEffect } from "react";
import axios from 'axios';
import Navbar from "../components/navbar";
import User from "../components/user";
import Icon from "../components/icon";
import Search from "../components/search";
import TableRobo from "../components/tableRobo";
import styles from "../styles/Navigate.module.css";
import Image from "next/image";
import "../globals.css";
import ChatbotModal from "../components/chatbotModal";

export default function History() {
  const [isChatbotModalOpen, setIsChatbotModalOpen] = useState(false);

  const handleOpenChatbotModal = () => {
    setIsChatbotModalOpen(true);
  };

  const handleCloseChatbotModal = () => {
    setIsChatbotModalOpen(false);
  }

  return (
    <>
      <Navbar />
      <div className={styles.userInfo}>
        <span className={styles.userName}>Itinerário Percorrido pelo Robô</span>
      </div>
      <div className={styles.mainContainer}>
        <div className={styles.tableContainer}>
          < TableRobo />
        </div>
      </div>
      <button onClick={handleOpenChatbotModal}>
        <Icon />
      </button>
      {isChatbotModalOpen && <ChatbotModal onClose={handleCloseChatbotModal} />}
    </>
  );
}
