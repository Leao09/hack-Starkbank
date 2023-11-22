"use client";
import Navbar from '../components/navbar';
import User from '../components/user';
import Icon from '../components/icon';
import Table from '../components/table';
import Image from 'next/image';
import styles from '../styles/History.module.css';
import '../globals.css';


export default function History() {

    return (
      <>
        <Navbar />
        <User />
        <div className={styles.wareHouseInfo}>
          <img className={styles.wareHouseImg} src="/wareHouse.png" alt="Foto de Perfil" />
          <div className={styles.titleDescription}>
            <span className={styles.wareHouseTitle}>Almoxarifado</span>
            <span className={styles.wareHouseDescription}>Ambev</span>
          </div>
        </div>
        <Table />
        <Icon />
      </>
    );
  }