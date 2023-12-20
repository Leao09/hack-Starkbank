'use client'
import React, { useState, useEffect } from "react";
import axios from 'axios';
import Navbar from "../components/navbar";
import User from "../components/user";
import Icon from "../components/icon";
import Search from "../components/search";
import Table from "../components/table_Wh";
import styles from "../styles/SearchPage.module.css";
import "../globals.css";
import ChatbotModal from "../components/chatbotModal";

export default function SearchPage() {
  const [isChatbotModalOpen, setIsChatbotModalOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [data, setData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/warehouse')
      .then(response => {
        setData(response.data);
        setFilteredData(response.data);
      })
      .catch(error => console.error('Erro ao obter dados:', error));
  }, []);

  const handleOpenChatbotModal = () => {
    setIsChatbotModalOpen(true);
  };

  const handleCloseChatbotModal = () => {
    setIsChatbotModalOpen(false);
  };

  const handleSearchChange = (event) => {
    const value = event.target.value;
    setSearchTerm(value);
    const filtered = data.filter(item => item.Name.toLowerCase().includes(value.toLowerCase()));
    setFilteredData(filtered);
  };

  return (
    <>
      <Navbar />
      <User />
      <div className={styles.wareHouseInfo}>
        <img
          className={styles.wareHouseImg}
          src="/wareHouse.png"
          alt="Foto de Perfil"
        />
        <div className={styles.titleDescription}>
          <span className={styles.wareHouseTitle}>Almoxarifado</span>
          <span className={styles.wareHouseDescription}>Ambev</span>
        </div>
      </div>
      <div className={styles.mainContainer}>
        <div className={styles.searchBarContainer}>
          <Search onChange={handleSearchChange} />
        </div>
        <div className={styles.tableContainer}>
          <Table data={filteredData} />
        </div>
      </div>
      <button onClick={handleOpenChatbotModal}>
        <Icon />
      </button>
      {isChatbotModalOpen && <ChatbotModal onClose={handleCloseChatbotModal} />}
    </>
  );
}
