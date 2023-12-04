'use client';
import styles from '../styles/Modal.module.css'
import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css'; 

interface ModalProps {
  onClose: () => void;
}

const Modal: React.FC<ModalProps> = ({ onClose }) => {

  const [id, setId] = useState('');
  const [name, setName] = useState('');
  const [document, setDocument] = useState('');
  const [date, setDate] = useState<Date | null>(null);

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
        <div className={styles.backdrop}> </div>
        <div className={styles.modal} id="modal">
        <div className={styles.modalHeader}>
            Nova Requisição
        </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Id SAS:</label>
                <input autoComplete="off" type="text" className={styles.inputField} id="id" value={id} onChange={(e) => setId(e.target.value)}/>
            </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Nome:</label>
                <input autoComplete="off" type="text" className={styles.inputField} id="name" value={name} onChange={(e) => setName(e.target.value)}/>
            </div>
            <div className={styles.inputContainer}>
                <label className={styles.label}>Documento:</label>
                <input autoComplete="off" type="text" className={styles.inputField} id="document" value={document} onChange={(e) => setDocument(e.target.value)}/>
            </div>
            <div className={styles.inputContainer}>
                <label className={styles.labelDatePicker}>Data:</label>
                <DatePicker autoComplete="off" selected={date} className={styles.inputFieldDatePicker} id="date" onChange={(date: Date | null) => setDate(date)} dateFormat="dd/MM/yyyy" />
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