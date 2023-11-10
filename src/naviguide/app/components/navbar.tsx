import Link from 'next/link';
import Image from 'next/image';
import styles from '../styles/Navbar.module.css';

const Navbar = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <Image src="/logo.png" alt="Logo" width={166} height={50} />
      </div>
      <div className={styles.navItems}>
          <a className={styles.navItem}>Home</a>
          <a className={styles.navItem}>Histórico</a>
          <a className={styles.navItem}>Perfil</a>
          <a className={styles.navItem}>Navegação</a>
      </div>
    </nav>
  );
};

export default Navbar;
