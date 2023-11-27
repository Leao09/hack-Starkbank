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
        <Link href="/home" className={styles.navItem}>
          Home
        </Link>
        <Link href="/history" className={styles.navItem}>
          Histórico
        </Link>
        <Link href="/profile" className={styles.navItem}>
          Perfil
        </Link>
        <Link href="/navigate" className={styles.navItem}>
          Navegação
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
