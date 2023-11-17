import Image from 'next/image';
import styles from './styles/PrimeiraTela.module.css';
import Link from 'next/link';

export default function PrimeiraTela() {
  return (
    <div className={styles.container}>
      <div className={styles.mainContent}>
      <Link href="/home" passHref>
        <button className={styles.button}>
          <span>Iniciar</span>
        </button>
      </Link>
        <Image src="/directions.png" alt="Directions" width={219} height={185} className={styles.imageDirections} />
        <div className={styles.titleContainer}>
          <div className={styles.title}>NaviGuide</div>
          <p className={styles.description}>
            Seu assistente de buscas <br />
            no almoxarifado
          </p>
        </div>
        <div className={styles.robotImageContainer}>
          <div className={styles.robotImageBackground} />
          <Image src="/robotTalk.png" alt="Robot Talking" width={667} height={304} className={styles.robotImage} />
        </div>
      </div>
    </div>
  );
};
