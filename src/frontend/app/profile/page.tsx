"use client";
import React, { useState,FormEvent } from 'react';
import Image from 'next/image';
import Navbar from '../components/navbar';
import Icon from '../components/icon';
import styles from '../styles/Profile.module.css'; 
import { FaEye, FaEyeSlash } from 'react-icons/fa';
import '../globals.css';
import ChatbotModal from '../components/chatbotModal';


export default function Profile() {

    const [showPassword, setShowPassword] = useState(false);

    const [isChatbotModalOpen, setIsChatbotModalOpen] = useState(false);

    const handleOpenChatbotModal = () => {
      setIsChatbotModalOpen(true);
    };
  
    const handleCloseChatbotModal = () => {
      setIsChatbotModalOpen(false);
    };

    const togglePasswordVisibility = () => {
      setShowPassword(showPassword => !showPassword);
    };

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
  
    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
      e.preventDefault();
  };

    return (
      <>
        <Navbar />
        <div className={styles.container}>
          <div className={styles.leftContainer}>
            <div className={styles.perfilContainer}>

              <form className={styles.userForm} onSubmit={handleSubmit}>
              <div className={styles.userInfo}>
                <Image src="/profile.png" alt="Foto de Perfil" width={80} height={80} />
                <span className={styles.userName}>Perfil</span>
              </div>
              <div className={styles.formRow}>
                <div className={styles.formGroup}>
                  <label className={styles.label} htmlFor="firstName">Primeiro Nome</label>
                  <input
                    id="firstName"
                    type="text"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                  />
                </div>

                <div className={styles.formGroup}>
                  <label className={styles.label} htmlFor="lastName">Sobrenome</label>
                  <input
                    id="lastName"
                    type="text"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                  />
                </div>
              </div>

                <label className={styles.label} htmlFor="id">Identificação</label>
                <input
                  id="id"
                  type="text"
                  value={id}
                  onChange={(e) => setId(e.target.value)}
                />

                <label className={styles.label} htmlFor="password">Senha</label>
                <div className={styles.passwordGroup}>
                  <input
                    id="password"
                    type={showPassword ? "text" : "password"}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                  <i onClick={togglePasswordVisibility} className={styles.eyeIcon}>
                    {showPassword ? <FaEyeSlash /> : <FaEye />}
                  </i>
                </div>

                <button type="submit">Salvar Alterações</button>
              </form>
            </div>
          </div>
          <div className={styles.rightContainer}>
            <img src="/profileGraph.png" alt="Foto pessoa" />
          </div>
        </div>
        <button onClick={handleOpenChatbotModal}>
          <Icon />
        </button>
        {isChatbotModalOpen && <ChatbotModal onClose={handleCloseChatbotModal} />}
      </>
    );
  }