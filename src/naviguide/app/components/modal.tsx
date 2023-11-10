'use client';
import styles from '../styles/Modal.module.css'
import React, { useState } from 'react';

interface ModalProps {
  onClose: () => void;
}

const Modal: React.FC<ModalProps> = ({ onClose }) => {

  const [id, setId] = useState('');
  const [name, setName] = useState('');
  const [document, setDocument] = useState('');
  const [date, setDate] = useState('');

  const handleConfirm = () => {
    const formData = {
      id,
      name,
      document,
      date
    };
    console.log(formData);

    onClose();
  }
  
  return (
    <>
        <div className={styles.backdrop} onClick={onClose}></div>
        <div className={styles.modal} id="modal">
        <div className={styles.modalHeader}>
            Nova Requisição
        </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Id SAS:</label>
                <input type="text" className={styles.inputField} id="id" value={id} onChange={(e) => setId(e.target.value)}/>
            </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Nome:</label>
                <input type="text" className={styles.inputField} id="name" value={name} onChange={(e) => setName(e.target.value)}/>
            </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Documento:</label>
                <input type="text" className={styles.inputField} id="document" value={document} onChange={(e) => setDocument(e.target.value)}/>
            </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Data:</label>
                <input type="text" className={styles.inputField} id="date" value={date} onChange={(e) => setDate(e.target.value)}/>
            </div>
            <div className={styles.modalFooter}>
                <button className={`${styles.button} ${styles.cancelButton}`} onClick={onClose}>Cancelar</button>
                <button className={`${styles.button} ${styles.registerButton}`} onClick={handleConfirm}>Enviar</button>
            </div>
        </div>
        </>
    );
}

export default Modal;