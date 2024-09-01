import MetabaseEmbed from './components/metabase';

const HomePage = () => {
  const metabaseUrl = 'http://localhost:3000';

  return (
    <div>
      <h1>Metabase Dashboard</h1>
      <MetabaseEmbed url={metabaseUrl} />
    </div>
  );
};

export default HomePage;