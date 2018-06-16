# coding:utf-8

import json
from flask import url_for

from rmon.models import Server

class TestServerList:
    """
    ���� Redis �������б� API
    """
    endpoint = 'api.server_list'

    def test_get_servers(self,server,client):
        """
        ��ȡ Redis�������б�
        """
        resp = client.get(utl_for(self.endpoint))

        # RestView ��ͼ��������� HTTP ͷ�� Content��TypeΪjson
        assert resp.headers['Content-Type'] == 'application/json; cahrset=utf-8'
        
        # ���ʳɹ��󷵻�״̬�� 200 ok
        assert resp.status_code == 200

        servers =resp.json

        # ���ڵ�ǰ���Ի�����ֻ��һ�� Redis �����������Է��ص�����Ϊ1 
        assert len(servers) == 1

        h = servers[0]
        assert h['name'] == server.name
        assert h['description'] == server.description
        assert h['host'] == server.host
        assert h['port'] == server.port
        assert 'updated_at' in h
        assert 'created_at' in h

    def test_create_server_success(self,db,client):
        """
        ���Դ���Redis�������ɹ�
        """
        # ���в���
        pass

    def test_create_server_failed_with_invalid_host(self,db,client):
        """
        ��Ч�ķ�������ַ���´��� Redis ������ʧ��
        """
        #  ���в���
        pass

    def test_create_server_failed_with_duplciate_server(self,server,client):
        """
        �����ظ��ķ�����ʱ��ʧ��
        """
        # ���в���
        pass



class TestServerDetail:
    """
    ����Redis����������API
    """
    endpoint = 'api.server_detail'

    def test_get_server_success(self,server,client):
        """
        ���Ի�ȡ Redis ����������
        """
        pass

    def test_get_server_failed(self,db,client):
        """
        ��ȡ�����ڵ�Redis����������ʧ��
        """
        pass

    def test_update_server_success(self,server,client):
        """
        ���� Redis �������ɹ�
        """
        pass

    def test_update_server_success_with_duplicate_server(self,server,client):
        """
        ���·���������Ϊ����ͬ������������ʱʧ��
        """
        pass

    def test_delete_success(self,server,client):
        """
        ɾ�� Redis �������ɹ�
        """
        pass

    def test_delete_failed_with_host_not_exist(self,db,client):
        """
        ɾ�� �����ڵ�Redis������ʧ��
        """
        pass



