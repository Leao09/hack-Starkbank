"use client";
import Navbar from '../components/navbar';
import User from '../components/user';
import Icon from '../components/icon';
import Search from '../components/search';
import Table from '../components/table';
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
        <div className={styles.mainContainer}>
          <div className={styles.searchBarContainer}>
            <Search />
          </div>
          <div className={styles.tableContainer}>
            <Table />
          </div>
        </div>
        <Icon />
      </>
    );
  }