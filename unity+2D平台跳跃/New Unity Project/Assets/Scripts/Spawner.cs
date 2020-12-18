using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public float spawnTime;
    private float countTime;
    private Vector3 spawnPosition;
    public List<GameObject> platforms =  new List<GameObject>();
    // Start is called before the first frame update
    // Update is called once per frame
    void Update()
    {
        SpawnPlatform();
    }

    public void SpawnPlatform()
    {
        countTime += Time.deltaTime;
        spawnPosition = transform.position;
        spawnPosition.x = Random.Range(-3.5f,3.5f);

        if (countTime >= spawnTime)
        {
            CreatePlatform();
            countTime = 0;
        }

    }

    public void CreatePlatform()
    {
        int index = Random.Range(0,platforms.Count);
        Instantiate(platforms[index],spawnPosition,Quaternion.identity);

    }
}
