import React from 'react';

interface MetabaseEmbedProps {
  url: string;
  width?: string;
  height?: string;
}

const MetabaseEmbed = ({ url, width = '300%', height = '600px' }: MetabaseEmbedProps) => {
    const proxyUrl = `/metabase-proxy${url}`;
  return (
    <iframe
      src={proxyUrl}
      width={width}
      height={height}
      title="Metabase Embed"
    />
  );
};

export default MetabaseEmbed;