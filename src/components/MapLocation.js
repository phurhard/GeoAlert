import React, { useEffect, useState } from 'react';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

const MapLocation = ({ google }) => {
  const [location, setLocation] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        handleSuccess,
        handleError
      );
    } else {
      setError("Geolocation is not supported by your browser");
    }
  }, []);

  const handleSuccess = (position) => {
    const { latitude, longitude } = position.coords;
    setLocation({ latitude, longitude });
  };

  const handleError = (error) => {
    setError(`Geolocation error: ${error.message}`);
  };

  return (
    <div style={{ width: '50%', height: '400px' }}>
      {location ? (
        <Map
          google={google}
          zoom={5}
          initialCenter={{ lat: location.latitude, lng: location.longitude }}
          center={{ lat: location.latitude, lng: location.longitude }}
        >
          <Marker position={{ lat: location.latitude, lng: location.longitude }} />
        </Map>
      ) : (
        <p>{error || "Fetching location..."}</p>
      )}
    </div>
  );
};

export default GoogleApiWrapper({
  apiKey: 'AIzaSyARnQvoDVFy3Rld8bDIWEjOoRmwhuouEB0'
})(MapLocation);
