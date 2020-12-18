using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FlySpawner : MonoBehaviour
{
    public float spawnTime;
    private float countTime;
    private Vector3 spawnPosition;
    public List<GameObject> flys =  new List<GameObject>();
    // Start is called before the first frame update
    // Update is called once per frame
    void Update()
    {
        SpawnFly();
    }

    public void SpawnFly()
    {
        countTime += Time.deltaTime;
        spawnPosition = transform.position;
        spawnPosition.x = Random.Range(-3.5f,3.5f);
        transform.localEulerAngles = new Vector3(0,0,180);

        if (countTime >= spawnTime)
        {
            CreateFly();
            countTime = 0;
        }

    }

    public void CreateFly()
    {
        int index = Random.Range(0,flys.Count);
        Instantiate(flys[index],spawnPosition,Quaternion.identity);

    }
}

